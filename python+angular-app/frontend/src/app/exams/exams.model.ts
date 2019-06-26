export class Exam {
    constructor(
        public title: string,
        public description: string,
        public id?: number,
        public createdAt?: Date,
        public updatedAt?: Date,
        public lastUpdatedBy?: string
    ) {}
}
