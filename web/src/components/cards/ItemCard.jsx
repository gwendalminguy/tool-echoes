import { User, Guitar, Music } from "lucide-react";

function ItemCard({ cardClass, data, unit }) {
  const iconMap = {
    artists: User,
    genres: Guitar,
    titles: Music,
  };

  const IconComponent = iconMap[unit];

  if (!data) return <div className={cardClass}>No Data</div>;

  return (
    <div className={`${cardClass} flex flex-col items-center text-center gap-3`}>
      <div className="p-3 rounded-full bg-primary/20 text-primary">
        <IconComponent size={48} color="#4f46e5" />
      </div>
		  <span className="text-4xl font-semibold">
        {data.toLocaleString("fr-FR")}
      </span>
		  <span className="text-lg font-medium text-gray-500">
        {unit}
      </span>
    </div>
  );
}

export default ItemCard;
