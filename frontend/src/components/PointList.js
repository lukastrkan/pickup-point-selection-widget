import {Point} from "./Point";

export const PointList = (props) => {
    const {points, setSelectedPoint} = props;
    return (
        <div className={'overflow-auto'} style={{maxHeight: '100%'}}>
            {points !== null && points.map((point) => <Point key={point.id} point={point} setSelectedPoint={setSelectedPoint}/>)}
        </div>
    )
};