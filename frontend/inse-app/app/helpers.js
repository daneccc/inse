export const networkTypeHelper = function (value) {
    switch (value) {
        case 1:
            return "Federal";
        case 2:
            return "Estadual"
        case 3:
            return "Municipal"
        default:
            return "Outro"
    }
};

export const localeTypeHelper = function (value) {
    switch (value) {
        case 1:
            return "Urbana";
        case 2:
            return "Rural"
        default:
            return "Outro"
    }
};

export const capitalTypeHelper = function (value) {
    switch (value) {
        case 1:
            return "Capital";
        case 2:
            return "Interior"
        default:
            return "Outro"
    }
};