"use client";

import { useState } from "react";

export const LLMButton = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [submittedQuery, setSubmittedQuery] = useState(""); 
  const [isRickroll, setIsRickroll] = useState(false); 
  const [mediaType, setMediaType] = useState("Theory"); 

  const openModal = () => setIsOpen(true);
  const closeModal = () => {
    setIsOpen(false);
    setIsRickroll(false);
    setSubmittedQuery(""); 
  };

  const handleSearch = () => {
    setSubmittedQuery(searchQuery); 
    setSearchQuery(""); 
    setIsRickroll(true); 
  };

  return (
    <div>
      <button
        onClick={openModal}
        className="rounded-full bg-green-500 text-white px-6 py-2 mb-4"
      >
        Learn from LLM Music Teacher Agents!
      </button>

      {isOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
          onClick={closeModal}
        >
          <div
            className="bg-white p-8 rounded-lg shadow-lg max-w-3xl w-full"
            onClick={(e) => e.stopPropagation()} 
          >
            <h2 className="text-3xl font-semibold mb-6">Learn About Music</h2>
            <p className="mb-6">
              Hi! I'm your Music Teacher LLM Agent! Feel free to asny me any music related questions!
            </p>

            <div className="flex gap-3">
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Enter your search query"
                className="px-4 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
              />
              <select
                value={mediaType}
                onChange={(e) => setMediaType(e.target.value)}
                className="px-4 py-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="Technical">Technical</option>
                <option value="Theory">Theory</option>
              </select>
              <button
                onClick={handleSearch}
                className="bg-blue-500 text-white px-4 py-3 rounded-lg"
              >
                Search
              </button>
            </div>

            {submittedQuery && (
              <div className="mt-4 text-lg font-semibold text-gray-700">
                Search query: "{submittedQuery}"
              </div>
            )}

            {isRickroll && mediaType === "Technical" && (
              <div className="mt-6">
                Thank you for asking such a profound Technical question. The Music Teacher LLM is unfortunately not accessible at this time!
              </div>
            )}

            {isRickroll && mediaType === "Theory" && (
              <div className="mt-6 flex justify-center">
                Thank you for asking such a profound Theory question. The Music Teacher LLM is unfortunately not accessible at this time!
              </div>
            )}

            <div className="flex justify-center mt-6">
              <button
                onClick={closeModal}
                className="bg-green-500 text-white px-5 py-3 rounded-lg"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
