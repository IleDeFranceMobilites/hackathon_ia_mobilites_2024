import Hello from "@/app/components/hello";
import { Button } from "@/components/ui/button";

export default function Home() {
  console.log("Hello Server");

  return (
    <>
      <div className="text-3xl">Hello</div>
      <Hello />
      <Button>Click me</Button>
    </>
  );
}
