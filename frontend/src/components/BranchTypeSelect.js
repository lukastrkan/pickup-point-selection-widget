import {Form} from "react-bootstrap";

export const BranchTypeSelect = ({branchTypes, selectBranchType, staticBranchType}) => {
    if (staticBranchType) {
        return null;
    }
    return (<Form.Select onChange={(e) => {
            selectBranchType(e.target.value)
        }}
                         defaultValue={branchTypes.length > 0 ? branchTypes[0].id : null}>
            {branchTypes.map((type, index) => {
                return <option key={index} value={type.id}>{type.name} ({type.id})</option>
            })}
        </Form.Select>)
}