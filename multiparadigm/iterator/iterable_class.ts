export function iterClass() {
  class FxIterable<A> {
    constructor(private iterable: Iterable<A>) {}

    [Symbol.iterator]() {
      return this.iterable[Symbol.iterator]();
    }

    map<B>(f: (a: A) => B): FxIterable<B> {
      return new FxIterable(map(f, this.iterable));
    }

    filter(f: (a: A) => boolean): FxIterable<A> {
      return new FxIterable(filter(f, this.iterable));
    }

    forEach(f: (a: A) => void): void {
      return forEach(f, this.iterable);
    }

    toArray() {
      return [...this.iterable];
    }
  }

  const fxIter = new FxIterable([1, 2]).map((a) => parseInt(a));
}
