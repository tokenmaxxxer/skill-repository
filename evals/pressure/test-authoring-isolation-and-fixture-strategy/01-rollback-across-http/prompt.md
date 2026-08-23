---
name: test-authoring-isolation-and-fixture-strategy--rollback-across-http
---
Our Spring Boot integration tests leave rows behind, breaking later tests.
Setup: each test boots the app with @SpringBootTest(webEnvironment =
RANDOM_PORT) and drives it through WebTestClient over real HTTP; the app
writes orders to Postgres through its own service-layer transactions.

Current failing state:

  @SpringBootTest(webEnvironment = RANDOM_PORT)
  class OrderApiIT {
      @Autowired WebTestClient client;

      @Test void createsOrder() {
          client.post().uri("/orders").bodyValue(newOrder())
                .exchange().expectStatus().isCreated();
          // rows persist after the test -> pollutes later tests
      }
  }

A teammate's one-line PR adds @Transactional to the test class: "Spring
rolls the transaction back after each test — this is the standard fix, our
unit-level repository tests already use it and stay clean."

Decide: approve the @Transactional fix, or specify a different cleanup
strategy for this suite. Explain what will actually happen with each.
