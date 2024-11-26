import type { Metadata } from "next";
import "./globals.scss";

export const metadata: Metadata = {
  title: "ACCIT",
  description: "Accessible Itininerary",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`font-body antialiased`}>{children}</body>
    </html>
  );
}
