export function lec() {
  function forEach<A>(f: (a: A) => void, iterable: Iterable<A>) {
    const iterator = iterable[Symbol.iterator]();
    while (true) {
      const { done, value } = iterator.next();
      if (done) break;
      f(value);
    }
  }

  function map<T, U>(
    f: (value: T) => U,
    iterable: Iterable<T>
  ): IterableIterator<U> {
    const iterator = iterable[Symbol.iterator]();
    return {
      next(): IteratorResult<U> {
        const { done, value } = iterator.next();
        return done ? { done, value } : { done, value: f(value) };
      },
      [Symbol.iterator]() {
        return this;
      },
    };
  }

  function filter<T, U>(f: (value: T) => U, iterable: Iterable<T>) {
    const iterator = iterable[Symbol.iterator]();
    return {
      next() {
        while (true) {
          const { done, value } = iterator.next();
          if (done) return { done, value };
          if (f(value)) return { done, value };
        }
      },
      [Symbol.iterator]() {
        return this;
      },
    };
  }
}
