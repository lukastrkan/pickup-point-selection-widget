import {Card} from "react-bootstrap";
import {BoxSeam, CreditCard, PersonWheelchair, Shop} from "react-bootstrap-icons";

export const Point = (props) => {
    const {point, setSelectedPoint} = props;
    return (<Card onClick={() => {
            setSelectedPoint(point)
        }}>
            <Card.Body>
                <Card.Title>{point.name}</Card.Title>
                <Card.Subtitle className="mb-2 text-muted">{point.address}</Card.Subtitle>
                <Card.Text>
                        <span className={'me-2'}>
                            {point.box ? <BoxSeam title={'Výdejní box'}/> : <Shop title={'Pobočka'}/>}
                        </span>
                    <span className={'me-2'}>
                            {point.card ? <CreditCard title={'Karta'}/> : <CreditCard title={'Karta'} color={'grey'}/>}
                        </span>
                    <span className={'me-2'}>
                            {point.wheelchair ? <PersonWheelchair title={'Bezbariérový přístup'}/> :
                                <PersonWheelchair title={'Bezbariérový přístup'} color={'grey'}/>}
                        </span>
                </Card.Text>
            </Card.Body>
        </Card>)
}