// Last updated: 28/05/2025, 21:04:40
/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = new Map()
    return function(...args) {
        const argsKey = JSON.stringify(args)
        if (cache.has(argsKey)) {
            return cache.get(argsKey)
        }
        const result = fn(...args);
        cache.set(argsKey, result)
        return result
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */