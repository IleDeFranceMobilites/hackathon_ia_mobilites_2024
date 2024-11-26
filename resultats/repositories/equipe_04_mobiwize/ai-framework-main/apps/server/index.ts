import express from 'express';
import WebSocket from "ws";
import {graphRag} from "@repo/ai-toolkit/graphs/rag";

// Message type definitions
interface BaseMessage {
  type: string;
  payload: any;
}

interface UserMessage extends BaseMessage {
  type: 'USER_MESSAGE';
  payload: {
    content: string;
  };
}

interface ToolUpdate extends BaseMessage {
  type: 'TOOL_UPDATE';
  payload: {
    toolName: string;
    data: any;
  };
}

interface SystemMessage extends BaseMessage {
  type: 'SYSTEM_MESSAGE';
  payload: {
    status: string;
    message: string;
  };
}

type WebSocketMessage = UserMessage | ToolUpdate | SystemMessage;

const app = express();

// Create WebSocket server
const wss = new WebSocket.Server({port: 9998});

// Broadcast to all connected clients
const broadcast = (message: any) => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(message));
    }
  });
};

const processRagStream = async (content: string) => {
  try {
    for await (const chunk of await graphRag.stream({
      messages: [{role: "user", content}]
    }, {
      configurable: {
        thread_id: "1"
      },
      streamMode: "updates",
    })) {
      for (const [node, values] of Object.entries(chunk)) {
        console.log(`Receiving update from node: ${node}`);

        // Broadcast node updates
        broadcast({
          type: 'NODE_UPDATE',
          payload: {
            node,
            values
          }
        });
      }
    }
  } catch (error) {
    console.error('Error processing RAG stream:', error);
    broadcast({
      type: 'SYSTEM_MESSAGE',
      payload: {
        status: 'error',
        message: 'Error processing request'
      }
    });
  }
};

// Message handlers
const messageHandlers = {
  USER_MESSAGE: async (payload: UserMessage['payload'], ws: WebSocket) => {
    console.log('Processing user message:', payload.content);
    await processRagStream(payload.content);
  },

  TOOL_UPDATE: (payload: ToolUpdate['payload'], ws: WebSocket) => {
    console.log(`Tool update received from ${payload.toolName}:`, payload.data);
  },

  SYSTEM_MESSAGE: (payload: SystemMessage['payload'], ws: WebSocket) => {
    console.log('System message:', payload.message);
    broadcast({
      type: 'SYSTEM_MESSAGE',
      payload
    });
  }
};

// WebSocket connection handler
wss.on('connection', (ws: WebSocket) => {
  console.log('New client connected');

  // Message handler
  ws.on('message', async (message: string) => {
    try {
      const parsedMessage = JSON.parse(message) as WebSocketMessage;

      if (messageHandlers[parsedMessage.type]) {
        await messageHandlers[parsedMessage.type](parsedMessage.payload as any, ws);
      } else {
        ws.send(JSON.stringify({
          type: 'SYSTEM_MESSAGE',
          payload: {
            status: 'error',
            message: `Unsupported message type: ${parsedMessage.type}`
          }
        }));
      }
    } catch (error) {
      console.error('Error processing message:', error);
      ws.send(JSON.stringify({
        type: 'SYSTEM_MESSAGE',
        payload: {
          status: 'error',
          message: 'Error processing message'
        }
      }));
    }
  });

  // Error handler
  ws.on('error', (error) => {
    console.error('WebSocket error:', error);
  });

  // Disconnection handler
  ws.on('close', () => {
    console.log('Client disconnected');
  });
});

// Express routes
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start server
app.listen(9999, () => {
  console.info(`Express server listening on port 9999`);
  console.info(`WebSocket server listening on port 9998`);
});
