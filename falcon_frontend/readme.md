# Falcon frontend

The left menu corresponds to settings. Graph information is displayed on the right side; this is the data loaded from the database. The form to select a route is preloaded with information from the database. Next, when the odds are computed there is a graph that changes the text to white to draw a path from the source to the target.### Run with docker

```
 $ docker build  -t falcon-frontend .
 $ docker run -p 4200:4200  -t falcon-frontend
 # ***recommend to use chrome some browsers like brave can block the api request***
```

## Setup for development

### Run the application

```
 $ npm install
 # use a version of node greater than 18 otherwise it may fail
 # I use nvm v18.19
 $ npx nx serve falcon_frontend
```

### Run the tests

```
 $ npx nx test falcon_frontend
```

### run e2e tests

```sh
    $ npx nx e2e e2e
```

## Build for production

```
 $ npx nx build falcon_frontend
```

## Explore the project graph

```
 $ npx nx dep-graph
```

  <div class="desc">
    <div>
      You have a graph with N nodes and M edges. A person wants to travel from
      node Ni to node Nj. They can only travel along an edge if their autonomy E
      is greater than the edge’s weight. When they reach a node, they can
      recharge their energy, but it takes an extra day. They can also choose to
      continue without recharging. On certain days, thieves are present at some
      nodes. The risk of being killed increases each time the person passes
      through or stops at these nodes. This risk follows the formula:
    </div>
    <div>
      P(to be killed) = 1/10 + 9/10^2 + 9^2/10^3 + 9^3/10^4 + ... + 9^(k-1)/10^k
      where k is the number of times the thieves try to kill the person.
    </div>
    <div>
      The person must arrive before the countdown units otherwise it will die.
    </div>
    <ul>
      <li>
        What is the probability that the person arrives at the destination
        safely?
      </li>
      <li>
        If can arrive, how long does it take to arrive to the destination ?
      </li>
    </ul>
  </div>