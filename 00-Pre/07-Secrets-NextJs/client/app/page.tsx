"use client";
import { useState } from "react";
import TextArea from "./_components/textarea";

export default function Home() {
  const [token, setToken] = useState("");
  const [pods, setPods] = useState([]);

  async function loaddata() {
    let response;

    response = await fetch("/api/pods", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ token }),
    });

    if (response.ok) {
      const data = await response.json();
      console.log(data);
      setPods(data);
    }
    console.log(pods);
  }
  return (
    <div className="max-w-3xl mx-auto py-8 space-y-4">
      <p className="font-medium text-2xl ">My dashboard</p>
      <TextArea updateValue={(v) => setToken(v)} />
      <button
        className="px-4 py-2 text-sm bg-blue-600 hover:bg-blue-600/40 hover:backdrop-blur-sm shadow-md text-white rounded-md ring-1 ring-white "
        onClick={() => loaddata()}
      >
        Load data
      </button>
    </div>
  );
}
