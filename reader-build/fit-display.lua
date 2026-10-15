-- Preserve the source expression; only constrain its rendered width to the page.
function Math(el)
  if FORMAT:match('latex') and el.mathtype == 'DisplayMath' then
    return pandoc.RawInline('latex', '\\[\\adjustbox{max width=\\linewidth}{$\\displaystyle ' .. el.text .. '$}\\]')
  end
  return el
end
