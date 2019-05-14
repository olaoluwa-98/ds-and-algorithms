class Queue {
  constructor() {
    this._queue = [];
  }
  /**
   * Adds a new item to the end of the queue
   * @method enqueue
   */
  enqueue(item) {
    this._queue.unshift(item);
  }
  /**
   * Removes the item in fron of the queue
   * @method dequeue
   */
  dequeue() {
    return this._queue.pop();
  }
  /**
   * Returns the item in front of the queue
   * @method peek
   */
  peek() {
    return this._queue[this._queue.length - 1];
  }
  /**
   * Returns the current length of the queue
   * @method length
   *
   * @return {Number}
   */
  get length() {
    return this._queue.length;
  }

  /**
   * Returns true if the queue is empty
   * @method isEmpty
   *
   * @return {Boolean}
   */
  isEmpty() {
    return this._queue.length === 0;
  }
}

module.exports = Queue;
