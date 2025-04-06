function groceriesList() {
  const groceries = [
    { name: "Apples", quantity: 10 },
    { name: "Tomatoes", quantity: 10 },
    { name: "Pasta", quantity: 1 },
    { name: "Rice", quantity: 1 },
    { name: "Banana", quantity: 5 },
  ];

  const groceryList = groceries.map((item) => `${item.quantity} ${item.name}`);
  return groceryList.join(", ");
}