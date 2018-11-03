function bubbleSort(arr = []) {
  const N = arr.length;

  // if the length of the array is less than 2, no need to sort
  if (N < 2) {
    return arr;
  }
  // Traverse through all array elements
  for (let i = 0; i < N; i++) {
    let swapped = false;
    // Last i elements are already
    // in place
    for (let j = 0; j < N - i - 1; j++) {
      // traverse the array from 0 to
      // n - i - 1. Swap if the element
      // found is greater than the
      // next element
      if (arr[j] > arr[j + 1]) {
        [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        swapped = true;
      }
    }

    // IF no two elements were swapped
    // by inner loop, then break
    if (swapped == false) {
      break;
    }
  }

  return arr;
}

console.log('** BUBBLE SORT **\n');

// worst case scenario. array is in descending order
console.log('Worst case scenario');
const worstCaseData = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
console.log(`Data for worst case scenerio => ${worstCaseData}`);
console.log(`Result from worst case scenerio => 😤 ${bubbleSort(worstCaseData)}\n`);

// average case scenario.
console.log('Average case scenario');
const averageCaseData = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9];
console.log(`Data for average case scenerio => ${averageCaseData}`);
console.log(`Result from average case scenerio => 😁 ${bubbleSort(averageCaseData)}\n`);

// best case scenario.array is already sorted
console.log('Best case scenario');
const bestCaseData = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(`Data for best case scenerio => ${bestCaseData}`);
console.log(`Result from best case scenerio => 👌 ${bubbleSort(bestCaseData)}`);
