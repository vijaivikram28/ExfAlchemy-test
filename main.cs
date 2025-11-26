using System;
using Microsoft.Extensions.Logging;

public class HelloWorldController
{
    private readonly ILogger<HelloWorldController> _logger;

    public HelloWorldController(ILogger<HelloWorldController> logger)
    {
        _logger = logger ?? throw new ArgumentNullException(nameof(logger));
    }

    public void PrintHelloWorld()
    {
        try
        {
            _logger.LogInformation("Attempting to print Hello World message");
            Console.WriteLine("Hello World!");
            _logger.LogInformation("Hello World message printed successfully");
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "An error occurred while printing Hello World message");
            throw;
        }
    }

    public void Execute()
    {
        try
        {
            PrintHelloWorld();
        }
        catch (Exception ex)
        {
            _logger.LogCritical(ex, "Unhandled exception in Execute method");
            Environment.Exit(1);
        }
    }
}