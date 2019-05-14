// BREATH FIRST SEARCH FOR GRAPHS
function BFSgraph(graph, root) {
  // create a set of visited nodes
  let visited = [];

  // insert the root as the first item in the queue
  let queue = [root];

  // run while the queue is not empty
  while (queue.length > 0) {
    // remove the current node from the queue and add as a visited node
    const currentNode = queue.shift();
    visited.push(currentNode);
    // if the node has children and they are not
    // in the queue, add them
    for (let neigbour of graph[currentNode]) {
      if (!queue.includes(neigbour)) {
        queue.push(neigbour);
      }
    }
    console.log(`Visited ${visited}`);
    console.log(`Queue ${queue}`);
  }
  return visited;
}

console.log('** BREATH FIRST SEARCH (BFS) FOR A GRAPH **\n');
const graph = { 5: [], 2: [4], 3: [4, 5], 4: [], 1: [2, 3] };
console.log('Graph =>');
console.log(graph);
console.log(`Nodes in thier order of visitation => ${BFSgraph(graph, 1)}`);

// // BREATH FIRST SEARCH FOR TREES

// // a class definition for type node
// class Node {
//   constructor(left, right) {
//     this.left = left;
//     this.right = right;
//   }
// }

// function BFStree(tree, root) {
//   // create a set of visited nodes
//   let visited = [];

//   // insert the root as the first item in the queue
//   let queue = [root];

//   // run while the queue is not empty
//   while (queue.length > 0) {
//     // remove the current vertex from the queue and add as a visited node
//     const vertex = queue.shift();
//     visited.push(vertex);
//     // if the node has children and they are not
//     // in the queue, add them
//     for (let neigbour of graph[vertex]) {
//       if (!queue.includes(neigbour)) {
//         queue.push(neigbour);
//       }
//     }
//   }
//   return visited;
// }

// console.log('** BREATH FIRST SEARCH (BFS) FOR A TREE **\n');
// const tree = {
//   1: new Node(2, 3),
//   2: new Node(4, 5),
//   3: new Node(3, 6, 7),
//   4: new Node(),
//   5: new Node(),
//   6: new Node(),
//   7: new Node(),
// };
// console.log(`Nodes in thier order of visitation => ${BFStree(tree, 1)}`);
