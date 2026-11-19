import { Suspense } from "react";

async function BackendStatus() {
  let backendStatus = "unknown";

  try {
    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/health`,
      { cache: "no-store" }
    );

    if (response.ok) {
      const data: { status: string } = await response.json();
      backendStatus = data.status;
    } else {
      backendStatus = "unavailable";
    }
  } catch {
    backendStatus = "unavailable";
  }

  return <p>Backend status: {backendStatus}</p>;
}

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center gap-4">
      <h1 className="text-3xl font-bold">TaskFlow AI</h1>

      <Suspense fallback={<p>Checking backend...</p>}>
        <BackendStatus />
      </Suspense>
    </main>
  );
}
