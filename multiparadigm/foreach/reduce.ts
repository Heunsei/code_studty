export function lec2() {
  function baseReduce<A, Acc>(
    f: (acc: Acc, a: A) => Acc,
    acc: Acc,
    iterator: Iterator<A>
  ) {
    while (true) {
      const { done, value: a } = iterator.next();
      if (done) break;
      acc = f(acc, a);
    }
    return acc;
  }

  function reduce<A, Acc>(
    f: (acc: A | Acc, a: A) => Acc,
    accOrIterable: Acc | Iterable<A>,
    iterable?: Iterable<A>
  ) {
    if (iterable === undefined) {
      iterable = accOrIterable as Iterable<A>;
      const iterator = iterable[Symbol.iterator]();
      const { done, value: acc } = iterator.next();
      if (done)
        throw new TypeError("reduce of empty iterable with no initial value");
      return baseReduce(f, acc, iterator) as Acc;
    } else {
      return baseReduce(f, accOrIterable as Acc, iterable[Symbol.iterator]());
    }
  }
}
