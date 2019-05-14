function linearSearch(arr, key) {
  for (let item of arr) {
    if (item === key) {
      return arr.findIndex(item);
    }
    return -1;
  }
}
