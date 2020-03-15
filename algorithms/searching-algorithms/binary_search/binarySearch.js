function binarySearch(arr, item) {
  let first = 0;
  let last = arr.length - 1;
  while (first <= last) {
    let midpoint = Math.round((first + last) / 2);
    if (arr[midpoint] === item) {
      return true;
    } else if (item < arr[midpoint]) {
      last = midpoint - 1;
    } else {
      first = midpoint + 1;
    }
  }
  return false;
}
