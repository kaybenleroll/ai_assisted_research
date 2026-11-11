-- Keep Pandoc's native section levels for numbering and stable fragment IDs.
-- The template supplies the document H1; expose sections one level below it
-- in the accessibility tree, including when JavaScript is disabled.
function Header(header)
  if FORMAT:match("html") then
    header.attributes["role"] = "heading"
    header.attributes["aria-level"] = tostring(header.level + 1)
  end
  return header
end
