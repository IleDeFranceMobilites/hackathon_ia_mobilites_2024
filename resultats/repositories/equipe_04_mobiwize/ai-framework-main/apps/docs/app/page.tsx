import {Button} from "@repo/ui/components/ui/button";
import {DirectoryLoader} from "langchain/document_loaders/fs/directory";
import {DocxLoader} from "@langchain/community/document_loaders/fs/docx";
import {RecursiveCharacterTextSplitter} from "langchain/text_splitter";


export default async function Page() {
  const inject = async () => {
    const loader = new DirectoryLoader(`${process.cwd()}/files`, {
      ".docx": (path) => new DocxLoader(path),
    })

    const textSplitter = new RecursiveCharacterTextSplitter({
      chunkSize: 500,
      chunkOverlap: 10,
    });

    const docs = await loader.load()
    const docSplitter = await textSplitter.splitDocuments(docs)

    // await Promise.all(docSplitter.map(async doc => {
    //   return vectorStore.addDocuments([doc])
    // }))

    console.log("done embeddings", docs.length)
  }

  await inject()

  return (
    <main>
      <Button>Click me</Button>
      <div>
        <pre>{JSON.stringify("events", null, 2)}</pre>
      </div>
    </main>
  );

}
