import {gql} from "@apollo/client";

export const GET_LOCATIONS = gql`query GetBranches($coordinatesA: CoordinatesInput, $coordinatesB: CoordinatesInput, $branchType: Int){
    branches(coordinatesA: $coordinatesA, coordinatesB: $coordinatesB, branchType: $branchType, country: "cz"){
        id,
        name,
        address,
        branchType{
            id
        },
        coordinates{
            latitude,
            longitude
        }
        box
        card
        wheelchair
    }
}`;

export const GET_BRANCH_TYPES = gql`query GetBranchTypes {
    branchTypes {
        id,
        name,
        icon
    }
}`;

export const GET_BRANCH_INFO = gql`query GetBranchInfo($id: Int!) {
    branch(id: $id) {
        address
        city
        coordinates {
            latitude
            longitude
        }
        country
        id
        name
        openningHours {
            friday
            monday
            saturday
            sunday
            thursday
            tuesday
            wednesday
        }
        zip
        branchId
    }
}`;

export const SEARCH_BRANCHES = gql`query SearchBranches($search: String!, $branchType: Int) {
  branches(search: $search, branchType: $branchType) {
    address
    city
    coordinates {
      latitude
      longitude
    }
    id
    name
    zip
    box
    card
    wheelchair
  }
}`

export const GET_CLUSTERS = gql`query ClusterQuery($coordinatesA: CoordinatesInput, $coordinatesB: CoordinatesInput, $branchType: Int, $zoom: Int!) {
  clusters(coordinatesA: $coordinatesA, coordinatesB: $coordinatesB, branchType: $branchType, zoom: $zoom) {
    id
    coordinates {
      latitude
      longitude
    }
    clusterZoom
    pointCount
    cluster
  }
}`
