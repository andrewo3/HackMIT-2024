import Image from "next/image";

export default function Home() {
  return (
    <div className="grid grid-rows-[1px_1fr_1fr_50px] items-center justify-items-center min-h-screen p-8 ">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-center">
        <img
          src="https://lh3.googleusercontent.com/d/1f_FS7UKUeTZxGdRaqkNsv6_GHEVO9SVs?authuser=1/view"
          alt="HackMIT logo"
          width={500}
          height={100}
        />
        <ol className="text-m text-center sm:text-center">
          <li> We've designed an LLM integrated music creator to lower the barrier of access to music literacy!</li>
          <li>We hope tools like these will help make learning music theory and music creation more accessible!</li>
        </ol>

        <div className="flex gap-3 items-center flex-col sm:flex-row">
          <a
            className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5"
            href="/pythonapp"
            rel="noopener noreferrer"
          >
            <Image
              className="dark:invert"
              src="https://nextjs.org/icons/vercel.svg"
              alt="Vercel logomark"
              width={20}
              height={20}
            />
            Try now!
          </a>
          <a
            className="rounded-full border border-solid border-black/[.08] dark:border-white/[.145] transition-colors flex items-center justify-center hover:bg-[#f2f2f2] dark:hover:bg-[#1a1a1a] hover:border-transparent text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 sm:min-w-44"
            href="https://ballot.hackmit.org/project/eaktb-keflw-gosws-ffajf"
            target="_blank"
            rel="noopener noreferrer"
          >
            See Project Overview
          </a>
        </div>
      </main>
      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
        <a
          className="flex items-center gap-1 hover:underline hover:underline-offset-4"
          href="https://docs.google.com/presentation/d/1BUaP3aMMtER53E-fQ03BLMHKME4uRtLiDee7pNIyqdk"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="https://nextjs.org/icons/file.svg"
            alt="File icon"
            width={16}
            height={16}
          />
          Presentation
        </a>
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="/pythonapp"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="https://nextjs.org/icons/window.svg"
            alt="Window icon"
            width={16}
            height={16}
          />
          The Project
        </a>
        <a
          className="flex items-center gap-2 hover:underline hover:underline-offset-4"
          href="https://github.com/andrewo3/HackMIT-2024"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Image
            aria-hidden
            src="https://nextjs.org/icons/globe.svg"
            alt="Globe icon"
            width={16}
            height={16}
          />
          See Our Git Repository →
        </a>
      </footer>
    </div>
  );
}
