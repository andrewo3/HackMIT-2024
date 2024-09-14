"use client";

import { useState } from "react";

export const InspireButton = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const [submittedQuery, setSubmittedQuery] = useState(""); 
  const [isRickroll, setIsRickroll] = useState(false); 
  const [mediaType, setMediaType] = useState("video"); 

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
        className="rounded-full bg-blue-500 text-white px-6 py-2 mb-4"
      >
        Get Some AI Inspiration!
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
            <h2 className="text-3xl font-semibold mb-6">Be Inspired!</h2>
            <p className="mb-6">
              Here's some AI-generated inspiration for your creative process! Keep pushing
              forward, and don't stop learning.
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
                <option value="video">Video</option>
                <option value="audio">Audio</option>
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

            {isRickroll && mediaType === "video" && (
              <div className="mt-6">
                <iframe
                  width="100%"
                  height="400"
                  src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1"//Would be an AI generated link from Suno outside proof of concept
                  title="YouTube video player"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen
                ></iframe>
              </div>
            )}

            {isRickroll && mediaType === "audio" && (
              <div className="mt-6 flex justify-center">
                <audio controls autoPlay>
                  <source
                    src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"//Would be an AI generated link from Suno outside proof of concept
                    type="audio/mpeg"
                  />
                  Your browser does not support the audio element.
                </audio>
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
