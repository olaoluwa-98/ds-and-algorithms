const Queue = require('../queue/queue');

class PriorityQueue {
  constructor() {
    this._highPriorityQueue = new Queue();
    this._lowPriorityQueue = new Queue();
  }
  /**
   * Adds a new item to the end of the queue
   * @method enqueue
   */
  enqueue(item, isHighPriority = false) {
    isHighPriority ? this._highPriorityQueue.enqueue(item) : this._lowPriorityQueue.enqueue(item);
  }
  /**
   * Removes the item in fron of the queue
   * @method dequeue
   */
  dequeue() {
    if (!this._highPriorityQueue.isEmpty()) {
      return this._highPriorityQueue.dequeue();
    }

    return this._lowPriorityQueue.dequeue();
  }
  /**
   * Returns the item in front of the queue
   * @method peek
   */
  peek() {
    if (!this._highPriorityQueue.isEmpty()) {
      return this._highPriorityQueue.peek();
    }

    return this._lowPriorityQueue.peek();
  }
  /**
   * Returns the current length of the queue
   * @method length
   *
   * @return {Number}
   */
  get length() {
    return this._highPriorityQueue.length + this._lowPriorityQueue.length;
  }

  /**
   * Returns true if the queue is empty
   * @method isEmpty
   *
   * @return {Boolean}
   */
  isEmpty() {
    return this._highPriorityQueue.isEmpty() && this._lowPriorityQueue.isEmpty();
  }
}

module.exports = PriorityQueue;
