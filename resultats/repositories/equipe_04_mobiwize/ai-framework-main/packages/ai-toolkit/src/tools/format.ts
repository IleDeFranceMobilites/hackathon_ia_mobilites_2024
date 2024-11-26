import {tool} from "@langchain/core/tools";

export const formatTool = tool(
  () => {

  },
  {
    name: "format_tool",
    description:
      "This tool should be called when the informations are available it can end the integration",
  }
)
