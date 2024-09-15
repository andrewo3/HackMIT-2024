"use client";

import { InspireButton } from "./inspire";
import { LLMButton } from "./llm";

export default function Home() {
  return (
    <div className="grid grid-rows-[1fr] items-center justify-items-center min-h-screen ">
      <main className="flex flex-col gap-4 items-center sm:items-center">
        <div className="flex flex-row gap-4 items-center">
         <InspireButton />
         <LLMButton />
        </div>
        <iframe
          src="http://localhost:8000"
          title="External Website"
          width="1000"
          height="600"
          style={{ border: "none" }}
        ></iframe>
      </main>
    </div>
  );
}
