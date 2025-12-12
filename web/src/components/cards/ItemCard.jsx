function ItemCard({ cardClass, icon, data, unit }) {

  if (!data) return <div className={cardClass}>No Data</div>;

  return (
    <div className={cardClass}>
      <h2 className="text-xl font-semibold mb-4">{name}</h2>
		  <span className="text-4xl font-semibold">{data}</span>
		  <span className="text-xl font-semibold"> {unit}</span>
    </div>
  );
}

export default ItemCard;
