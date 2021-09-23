class Queue {
  /**
   * Initializes internal array for the queue
   * @method constructor
   *
   * @return {void}
   */
  constructor() {
    this._queue = [];
  }

  /**
   * Adds a new item to the end of the queue
   * @method enqueue
   *
   * @return {Boolean}
   */
  enqueue(item) {
    this._queue.unshift(item);
    return true;
  }

  /**
   * Removes the item in front of the queue
   * @method dequeue
   *
   * @return {Boolean}
   */
  dequeue() {
    if (this.isEmpty()) return false;
    this._queue.pop();
    return true;
  }

  /**
   * Returns the item in front of the queue
   * @method peek
   *
   * @return {number | any}
   */
  peek() {
    if (this.isEmpty()) return -1;
    return this._queue[this._queue.length - 1];
  }

  /**
   * Returns the current length of the queue
   * @method length
   *
   * @return {number}
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
