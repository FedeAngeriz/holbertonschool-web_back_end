function createInt8TypedArray(length) {
    if (length < 0) {
        throw new RangeError('Position outside range');
    }
    return new Int8Array(length);
}
