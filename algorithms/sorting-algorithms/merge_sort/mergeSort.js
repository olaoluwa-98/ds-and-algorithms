function merge(leftArr = [], rightArr = []) {
  let result = [];
  let leftIndex = 0;
  let rightIndex = 0;

  while (leftIndex < leftArr.length && rightIndex < rightArr.length) {
    if (leftArr[leftIndex] < rightArr[rightIndex]) {
      result.push(leftArr[leftIndex]);
      leftIndex += 1;
    } else {
      result.push(rightArr[rightIndex]);
      rightIndex += 1;
    }
  }

  return [...result, ...leftArr.slice(leftIndex), ...rightArr.slice(rightIndex)];
}

function mergeSort(arr = []) {
  if (arr.length < 2) {
    return arr;
  }
  const mid = Math.round(arr.length / 2);
  const leftArray = arr.slice(0, mid);
  const rightArray = arr.slice(mid);
  return merge(mergeSort(leftArray), mergeSort(rightArray));
}

console.log('** MERGE SORT **\n');

// worst case scenario. array is in descending order
console.log('Worst case scenario');
const worstCaseData = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
console.log(`Data for worst case scenerio => ${worstCaseData}`);
console.log(`Result from worst case scenerio => 😤 ${mergeSort(worstCaseData)}\n`);

// average case scenario.
console.log('Average case scenario');
const averageCaseData = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6];
console.log(`Data for average case scenerio => ${averageCaseData}`);
console.log(`Result from average case scenerio => 😁 ${mergeSort(averageCaseData)}\n`);

// best case scenario.array is already sorted
console.log('Best case scenario');
const bestCaseData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(`Data for best case scenerio => ${bestCaseData}`);
console.log(`Result from best case scenerio => 👌 ${mergeSort(bestCaseData)}`);
