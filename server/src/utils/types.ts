export function isNone(variable : any) : boolean {
    return variable === null || variable === undefined;
}

export function arrayIsNoneOrEmpty(array : any[]) : boolean {
    return isNone(array) || array.length === 0;
}