export function calculateMaxDepth(urlsDict, depth = 0) {
  if (!urlsDict.founded_links || urlsDict.founded_links.length === 0) {
    return depth;
  }
  return Math.max(
    ...urlsDict.founded_links.map((link) =>
      calculateMaxDepth(link, depth + 1)
    )
  );
}
