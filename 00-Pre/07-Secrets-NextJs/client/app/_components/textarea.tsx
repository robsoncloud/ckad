"use client";

import { useRef, useState } from "react";
import useAutosizeTextArea from "./useAutosizeTextArea";

interface Props {
  updateValue: (data: string) => void;
}
const TextArea = ({ updateValue }: Props) => {
  const [value, setValue] = useState("");
  const textAreaRef = useRef<HTMLTextAreaElement>(null);
  useAutosizeTextArea(textAreaRef.current, value);

  const handleChange = (evt: React.ChangeEvent<HTMLTextAreaElement>) => {
    const val = evt.target?.value;

    setValue(val);
    updateValue(val)
  };

  return (
    <div>
      <textarea
        id="review-text"
        className="w-full rounded-lg outline-none p-4 text-zinc-600 shadow-sm drop-shadow-lg"
        onChange={handleChange}
        placeholder="Insert the token here"
        ref={textAreaRef}
        rows={1}
        value={value}
      />
    </div>
  );
};

export default TextArea;
