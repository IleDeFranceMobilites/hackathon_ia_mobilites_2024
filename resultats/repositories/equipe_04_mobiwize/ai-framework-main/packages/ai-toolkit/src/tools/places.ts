import {tool} from "@langchain/core/tools";
import {z} from "zod";
import process from "node:process";

interface PlacesResponse {
  places: Array<{
    id: string;
    name: string;
    type: string;
    distance?: string;
    administrative_regions?: Array<any>;
    geometry?: {
      coordinates: [number, number];
      type: string;
    };
  }>;
}

async function callPlacesAPI(params: {
  query: string;
  types?: string[];
  count?: number;
  from?: string;
}): Promise<PlacesResponse> {
  const searchParams = new URLSearchParams();
  searchParams.append('q', params.query);
  searchParams.append('disable_geojson', "true");

  console.log("callIDFMAPI for journeyPlannerTool", params)

  const response = await fetch(
    `https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/places?${searchParams.toString()}`,
    {
      headers: {
        'Accept': 'application/json',
        'apikey': process.env.PRIM_API_KEY
      } as HeadersInit
    }
  );

  if (!response.ok) {
    let res: string;
    try {
      res = JSON.stringify(await response.json(), null, 2);
    } catch (_) {
      res = await response.text();
    }
    throw new Error(`Failed to fetch places data.\nResponse: ${res}`);
  }

  return await response.json();
}

export const placesSearchTool = tool(
  async (input) => {
    try {

      const data = await callPlacesAPI({
        query: input.query,
      });
      return JSON.stringify(data, null, 2);
    } catch (e: any) {
      console.warn("Error fetching places data", e.message);
      return `An error occurred while fetching places data: ${e.message}`;
    }
  },
  {
    name: "places_search",
    description: "Searches for places in a specified region. Returns matching locations with their details. Use this tool to convert a location into a gps coordinates",
    schema: z.object({
      query: z.string().describe("Search query")
    })
  }
);
