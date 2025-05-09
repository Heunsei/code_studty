export function gen(): void {
  function* naturals(): Generator<number, void, ?> {
    let n: number = 1;
    while (true) {
      yield n++;
    }
  }

  function* reverse<T>(array: T[]): Generator<T, void, ?> {
    let i = array.length;
    while (i) {
      yield array[i--];
    }
  }

  function* map<A, B>(
    f: (value: A) => B,
    iterable: Iterable<A>
  ): IterableIterator<B> {
    for (const value of iterable) {
      yield f(value);
    }
  }

  function* filter<A>(
    f: (a: A) => boolean,
    iterable: Iterable<A>
  ): IterableIterator<A> {
    for (const a of iterable) {
      if (f(a)) {
        yield a;
      }
    }
  }
}
