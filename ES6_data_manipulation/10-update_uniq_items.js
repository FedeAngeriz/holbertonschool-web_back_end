function updateUniqueItems(items) {
  if (!Array.isArray(items)) {
    throw new Error('Invalid input');
  }

  const uniqueItems = new Set();
  const duplicates = new Set();

  for (const item of items) {
    if (uniqueItems.has(item)) {
      duplicates.add(item);
    } else {
      uniqueItems.add(item);
    }
  }

  for (const item of duplicates) {
    uniqueItems.delete(item);
  }

  return Array.from(uniqueItems);
}