import {FormControl, InputGroup} from "react-bootstrap";
import {Search as SearchIcon} from "react-bootstrap-icons";

export const Search = (props) => {
    const {handleSearch} = props;
    return (
        <InputGroup>
            <InputGroup.Text><SearchIcon/></InputGroup.Text>
            <FormControl type="text" placeholder="Vyhledávání" onChange={(e) => {
                if (e.target.value.length > 2 || e.target.value.length === 0) {
                    handleSearch(e.target.value)
                }
            }}/>
        </InputGroup>
    )
}