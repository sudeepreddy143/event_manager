# User Management System Documentation

## Project Overview

This repository contains a comprehensive user management system with robust data validation, enhanced security features, and bug fixes. The system provides reliable user profile management with strict input validation and edge case handling.

## Key Features and Fixes

1. [**Password Validation**](https://github.com/sudeepreddy143/event_manager/issues/3)

   * Comprehensive strength validation
   * Requirements for length, case, digits, and special characters
   * Implementation in user schema validation layer
   * [code](app\\\\schemas\\\\user_schemas.py)
2. [**Username Validation**](https://github.com/sudeepreddy143/event_manager/issues/1)

   * Nickname uniqueness verification
   * Real-time validation during profile updates
   * Prevention of duplicate user identifiers
   * [code](app\\\\services\\\\user_service.py)
3. [**Secure Password Handling**](https://github.com/sudeepreddy143/event_manager/issues/10)

   * Fixed method call in update service
   * Enhanced validation in update schema
   * Proper password management during user updates
   * [code](app\\\\schemas\\\\user_schemas.py)
4. [**Profile URL Validation**](https://github.com/sudeepreddy143/event_manager/issues/7)

   * Improved regex pattern for URL verification
   * Automatic HTTPS scheme addition when missing
   * Support for various valid URL formats
   * [code](app\\\\schemas\\\\user_schemas.py)
5. [**Content Length Validation**](https://github.com/sudeepreddy143/event_manager/issues/5)

   * Bio text character limit enforcement
   * Prevention of database constraint violations
   * User-friendly validation messages
   * [code](app\\\\schemas\\\\user_schemas.py)

## Docker Deployment

The application is containerized and available on DockerHub:
[docker.io/sudeeppanyam/event\_manager:latest](https://hub.docker.com/repository/docker/sudeeppanyam/event_manager/tags)

## Technical Implementation

The system is built using FastAPI and SQLAlchemy, providing a modern asynchronous API framework with robust database integration. The validation logic is implemented at multiple levels to ensure data integrity and security throughout the application flow.

### Architecture Highlights

* Multi-layered validation (schema and service level)
* Asynchronous API endpoints for improved performance
* Clear separation of concerns between validation and business logic

## Testing and Quality Assurance

Each feature and fix has been thoroughly tested with specific test cases to verify functionality. The codebase follows best practices for security and provides a solid foundation for further development.

this is updated repo

