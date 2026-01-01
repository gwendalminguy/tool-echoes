import { useEffect, useState } from "react";
import { DiscAlbum, User, Music, AudioLines } from "lucide-react";

function ItemCard({ cardClass, data, unit }) {
  const iconMap = {
    albums: DiscAlbum,
    artists: User,
    genres: Music,
    titles: AudioLines,
  };

  const IconComponent = iconMap[unit];
  const [displayValue, setDisplayValue] = useState(0);

  useEffect(() => {
    if (data == null) return;

    const duration = 500;
    const start = performance.now();
    const from = displayValue;
    const to = data;

    {/* Value Animation */}
    const animate = (now) => {
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const value = Math.round(from + (to - from) * eased);

      setDisplayValue(value);

      if (progress < 1) {
        requestAnimationFrame(animate);
      }
    };

    requestAnimationFrame(animate);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [data]);

  if (!data) return <div className={cardClass}>No Data</div>;

  return (
    <div className={`${cardClass} flex flex-col items-center text-center gap-1`}>
      <div className="p-5 rounded-full bg-primary/20 text-primary mb-5">
        <IconComponent size={48} color="#4f46e5" />
      </div>
		  <span className="text-4xl font-semibold">
        {displayValue.toLocaleString("fr-FR")}
      </span>
		  <span className="text-lg font-medium text-gray-500">
        {unit}
      </span>
    </div>
  );
}

export default ItemCard;
