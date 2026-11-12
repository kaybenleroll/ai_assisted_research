-- Keep Pandoc's native section levels for numbering and stable fragment IDs.
-- The filter sees source levels before any writer-level heading shift. The
-- template supplies the document H1, so retain source levels for sections in
-- the accessibility tree, including when JavaScript is disabled.
function Header(header)
  if FORMAT:match("html") then
    header.attributes["role"] = "heading"
    header.attributes["aria-level"] = tostring(header.level)
  end
  return header
end
