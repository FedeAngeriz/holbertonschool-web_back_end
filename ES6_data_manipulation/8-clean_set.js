function cleanSet(set, startString) {
  const result = [];
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  for (const item of set) {
    if (item && item.startsWith(startString)) {
      result.push(item.slice(startString.length));
    }
  }
  return result.join('-');
}
