"use client";
import { useState } from "react";

export default function Home() {
  const [token, setToken] = useState("");
  const [pods, setPods] = useState<[]>([]);
  const loadData = async () => {
    const response = await fetch("/api/pods", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ token }),
    });

    if (response.ok) {
      const data = await response.json();
      setPods(data);
    }
  };
  return (
    <div className="max-w-4xl mx-auto py-10 text-center space-y-4 ">
      <h1 className="text-2xl tracking-wider font-semibold text-pink-900">
        My Kubernetes Dashboard
      </h1>

      <textarea
        placeholder="token"
        className="w-full py-4 px-4 rounded-md outline-none drop-shadow-md text-zinc-500 tracking-widest placeholder:text-zinc-300"
        onChange={(e) => setToken(e.target.value)}
      />

      <button
        className="py-2 px-4 text-sm bg-pink-600 text-white font-semibold rounded-md hover:ring-2 shadow-sm active:scale-95 hover:bg-pink-500 transition-all ease-in-out ring-yellow-100"
        onClick={() => loadData()}
      >
        Load data
      </button>
    </div>
  );
}
