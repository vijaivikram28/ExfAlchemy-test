class HelloWorldController {
    constructor() {
        try {
            this.logger = console;
            this.execute();
        } catch (error) {
            this.handleError(error);
        }
    }

    execute() {
        try {
            this.printHelloWorld();
        } catch (error) {
            this.handleError(error);
        }
    }

    printHelloWorld() {
        try {
            console.log("Hello World");
        } catch (error) {
            this.handleError(error);
        }
    }

    handleError(error) {
        this.logger.error(`Error occurred: ${error.message}`);
        process.exit(1);
    }
}

new HelloWorldController();