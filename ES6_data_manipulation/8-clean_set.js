function cleanSet(set, startString) {
  if (typeof startString !== 'string' || !startString) {
    return '';
  }
  const filtered = Array.from(set)
  .filter(value => value.startsWith(startString))
  .map(value => value.slice(startString.length));

  return filtered.join('-');
}
