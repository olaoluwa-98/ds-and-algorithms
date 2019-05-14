function insertionSort(arr) {
  let n = arr.length;
  for (let i = 1; i < n; i++) {
    let midIndex = findMin(arr, i);
    let currntVal = arr[x];
    let pos = x;
    while (pos > 0 && arr[pos - 1] > currntVal) {
      arr[pos] = arr[pos - 1];
      pos -= 1;
    }
    arr[pos] = currntVal;
  }
  return arr;
}

function findMin(arr, start) {}
