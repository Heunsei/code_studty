export function iter(): void {
  class NumbersIterator<T> implements Iterator<T> {
    private index: number = 0;
    constructor(private array: T[]) {
      this.array = array;
    }
    next(): IteratorResult<T> {
      return this.index === this.array.length
        ? { done: true, value: undefined }
        : { done: false, value: this.array[this.index++] };
    }
  }

  // 무한히 이터레이터를 반환하는 함수.
  function naturals(end: number = Infinity): IterableIterator<number> {
    let i: number = 1;
    return {
      next(): IteratorResult<number, any> {
        return i <= end
          ? { done: false, value: i++ }
          : { done: true, value: undefined };
      },
      // Symbol.iterator를 return 하면 그 객체는 iterable
      [Symbol.iterator]() {
        return this;
      },
    };
  }

  // 원본을 변경하지 않고 지연성을 가지고 있음.
  function reverse<T>(array: T[]): Iterator<T> {
    let index: number = array.length;
    return {
      next(): IteratorResult<T, any> {
        return index === 0
          ? { done: true, value: undefined }
          : { done: false, value: array[--index] };
      },
    };
  }

  function map<A, B>(
    f: (a: A) => B,
    iterable: Iterable<A>
  ): IterableIterator<B> {
    const iterator = iterable[Symbol.iterator]();
    return {
      next(): IteratorResult<B, any> {
        const { done, value } = iterator.next();
        return done ? { done, value } : { done, value: f(value) };
      },
      [Symbol.iterator]() {
        return this;
      },
    };
  }

  const mapped = map((x:number) => x * 2, naturals(4));
  for (const num of mapped) {
    console.log(num);
  }
  new NumbersIterator([10, 20, 30]);
}

iter();