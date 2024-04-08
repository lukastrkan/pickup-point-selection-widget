import {ApolloClient, ApolloProvider, HttpLink, InMemoryCache} from "@apollo/client";
import React from "react";
import {Container} from "./components/Container";

const httpLink = new HttpLink({
    uri: '/graphql'
});

const client = new ApolloClient({
    cache: new InMemoryCache(),
    link: httpLink
});

function App(props) {
    return (
        <>
            <ApolloProvider client={client}>
                <Container position={props.position}/>
            </ApolloProvider>
        </>
    )
}

export default App;